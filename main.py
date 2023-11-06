# use python lib
import moviepy.editor as Mp4
# video file name
change = Mp4.VideoFileClip('Filename')
# audio file save name
change.audio.write_audiofile('save audio file name')
