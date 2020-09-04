import wave, struct
from array import *

def wavRead(fname):
    waveFile = wave.open(fname, 'r')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = waveFile.getparams()
    print ("======", nchannels, sampwidth, framerate, nframes, comptype, compname)
    frames = waveFile.readframes (nframes * nchannels)
    out = struct.unpack_from("%dh" % nframes * nchannels, frames)

    # Convert 2 channles to numpy arrays
    if nchannels == 2:
        left  = array (list (out[0::2]))
        right = array (list (out[1::2]))
    else:
        left = array('i', out)
        right = left
        
    print(len(left))

    n = 0
    frameSize = framerate/100
    cntStart = 0
    cntEnd = 0
    nFrames = len(left) / frameSize
    findStart = 0
    findEnd = 0
    Eng10 = []
    Eng10Sil = []
    Eng10Sil_avg = 0
    startFrame = 0
    endFrame = 0
    print("nFrames=", nFrames)

    for i in range(10):
        startPoint = i*frameSize
        endPoint = startPoint+frameSize
        
        eng = 0
        for j in range(frameSize):
            eng += left[startPoint+j] * left[startPoint+j] 
        eng /= (1.0 * frameSize)
        if len(Eng10Sil) == 10:
            del Eng10Sil[0]
        Eng10Sil += [eng]
        Eng10Sil_avg = sum(Eng10Sil)/10.0 #10
    print("Eng10Sil_avg=", Eng10Sil_avg)
    
    newName = fname.replace('.wav','')
    for i in range(nFrames):
        startPoint = i*frameSize
        endPoint = startPoint+frameSize
        
        eng = 0
        for j in range(frameSize):
            eng += left[startPoint+j] * left[startPoint+j] 
        eng /= frameSize
        if len(Eng10) == 10:
            del Eng10[0]
        Eng10 += [eng]
        Eng10_avg = sum(Eng10)/10
        #print "i=", i, startPoint, endPoint, Eng10_avg

        if not findStart:
            if Eng10_avg > Eng10Sil_avg * 3.0: #14500:
                cntStart += 1
                if cntStart >= 10:
                    findStart = 1
                    startFrame = max(0, i-25)
                    #print "----------------- startFrame=", startFrame
            else:
                cntStart = 0
        if findStart and i > startFrame+50 and not findEnd:
            if Eng10_avg > Eng10Sil_avg * 5.0: #15800:
                cntEnd = 0
            else:
                cntEnd += 1
                #print cntEnd, Eng10_avg
                if cntEnd > 25 or i == nFrames-1:
                    findEnd = 1
                    if cntEnd > 25:
                        endFrame = i #i-4
                    else:
                        endFrame = min(i, nFrames-1)
                    #print "----------------- cntEnd=", cntEnd, "endFrame=", endFrame
        if findEnd: 
            print("----n=", n, startFrame, endFrame)
            str_n = str(n)
            if n < 10:
                str_n = '_00' + str_n
            elif n < 100:    
                str_n = '_0' + str_n
            else:
                str_n = '_' + str_n
                
            outFileName = newName + '_0' + str_n + '.wav'
            ofile = wave.open(outFileName, 'w')
            #nchannels, sampwidth, framerate, nframes, comptype, compname
            #save only one channel
            ofile.setparams((1, sampwidth, framerate, 0, 'NONE', 'not compressed'))
            
            wvData=""
            for j in range((startFrame-1)*frameSize+1, endFrame*frameSize+1): 
                wvData += struct.pack('h', left[j]) 
            ofile.writeframes(wvData)
            ofile.close()
            cntStart = 0
            cntEnd = 0
            findStart = 0
            findEnd = 0

            n += 1
            
    waveFile.close()
    
filename = 'C:/VR_training/audio/LinXiao/CN_ori.wav' #'wy_nihao_20151022.wav' #xiaoyi.wav'
wavRead(filename)