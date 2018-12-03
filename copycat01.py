#!/usr/bin/env python3
#Retrieved stored away files
import shutil
#Targeting the os level functionality
import os
# Force python to start in the home user director
os.chdir('/home/student/mycode/')
#Copy single files
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# Copy entire folder including its individual files
shutil.copytree('5g_research/', '5g_research_backup/')
