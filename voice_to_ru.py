# pip install nemo_toolkit['all']

import nemo.collections.asr as nemo_asr

import torch

torch.cuda.empty_cache()


filenamebeg = "data/out"
fileend = ".wav"

for i in range(16):

    # torch.cuda.empty_cache()
    number = f"{i:03}"

    filename = filenamebeg + number + fileend
    outname = filenamebeg + number + ".txt"
    print(filename)

    asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(
        "nvidia/stt_ru_conformer_transducer_large"
    )

    output = asr_model.transcribe([filename])
    print(output[0].text)

    f = open(outname, "w", encoding="utf-8")
    f.write(output[0].text)
    f.close()


# ffmpeg -i 2025-03-17\ 12-14-05.mkv -vn -c:a libvorbis output.ogg
# ffmpeg -i input.ogg -acodec pcm_s16le -ac 1 -ar 16000 output.wav

# ffmpeg -i somefile.mp3 -f segment -segment_time 3 -c copy out%03d.mp3

#  ffmpeg -i audio_2025-03-26_21-49-00.ogg -acodec pcm_s16le -ac 1 -ar 16000 -f segment -segment_time 60 data/out%03d.wav
