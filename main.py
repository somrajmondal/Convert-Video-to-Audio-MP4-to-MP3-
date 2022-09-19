import moviepy.editor
Videofile= moviepy.editor.VideoFileClip('VIDEOSONG.mp4')  #or video file path
Audiofile=Videofile.audio
Audiofile.write_audiofile('onlyaudio.mp3')
