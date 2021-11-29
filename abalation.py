import glob

from image_finder import find_image
import time

dir_name = "small_dataset"
num_seen = 0
num_accurate = 0
num_time_sec = 0
files = glob.glob(dir_name+'/*/*.jpg')
num_files = len(files)
for filename in files:
    # print(filename)
    person_name = filename[len(dir_name)+1:]
    index = person_name.index("/")
    person_name = person_name[:index]
    person_name = person_name.replace("_"," ")
    # print(person_name)
    start = time.time()
    test_name = find_image(filename)
    end_time = time.time()
    print(person_name, test_name)
    if person_name == test_name:
        num_accurate += 1
    num_seen += 1

    num_time_sec += end_time-start
    print("("+str(num_seen)+"/"+str(num_files)+")Accuracy:"+str(num_accurate/num_seen))

print("Total time (s): "+str(num_time_sec))
print("Accuracy:"+str(num_accurate/num_seen))