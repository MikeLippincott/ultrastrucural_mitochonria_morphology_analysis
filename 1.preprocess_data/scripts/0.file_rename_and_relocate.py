#!/usr/bin/env python
# coding: utf-8

# This notebook renames the data files to have all files be in the same directory but with unique names.
# All files must be in the same directory for the CellProfiler pipeline to work.

# In[1]:


import pathlib

# In[2]:


# set path to data
data_path = pathlib.Path("../../data/").resolve(strict=True)
new_data_path = pathlib.Path("../../data/raw_images/").resolve()
# make new data directory if it doesn't exist
new_data_path.mkdir(parents=True, exist_ok=True)


# In[3]:


# get all files in data directory recursively
files = data_path.rglob("*")


# Rename the file names to incorporated the parent directory name into the file name.
# This is done to ensure that all files have unique names.

# In[4]:


# loop through the files
for file in files:
    if file.is_file():
        if file.suffix == ".tiff":
            new_file_name = (
                str(file.parents[0]).split("data/")[2].replace("/", "_")
                + "_"
                + file.stem
                + ".tiff"
            )
            new_file_path = pathlib.Path(f"{data_path}/raw_images/{new_file_name}")
            print(file, new_file_path)
            # rename file
            file.rename(new_file_path)