from readline import remove_history_item
import subprocess, sys
import yaml
from rosbag.bag import Bag
import os
import sys
import argparse
import shutil
import rospy

parser = argparse.ArgumentParser()
parser.add_argument("--target", help="the dir contains all the bag you wanna get csv")
args = parser.parse_args()

for f in os.listdir(args.target):
  if f.endswith(".bag"):
    # get the info of bag 
    info_dict = yaml.load(Bag(os.path.join(args.target, f), 'r')._get_yaml_info())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(info_dict['path'])
    path = info_dict['path']
    topics = open("topics.txt", "r")
    for topic in topics:
      print("-----------------------------------------------------------------")
      print("path :{}".format(path))
      print("topic :{}".format(topic.split(' ')[0]))
      print("csv :{}".format(path.replace('.bag', '_'+ topic.split()[1]+'.csv')))
      EXPRESSION = "rostopic echo -b "+path+" -p "+topic.split(' ')[0]+" > "+path.replace('.bag', '_'+ topic.split()[1]+'.csv')
      print("EXPRESSION :{}".format(EXPRESSION))
      subprocess.call([EXPRESSION],shell=True)
      print("-----------------------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

