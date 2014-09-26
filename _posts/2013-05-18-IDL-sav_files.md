---
layout: post
title: How to read IDL .sav files in Python
---

With my on-going effort to transition from IDL to Python, I present a post on reading IDL .sav files in Python. 

Make sure you have the latest version of Numpy and Scipy installed. 
Visit this page: IDL save file package and download the latest version of IDLSave file 
Open terminal and change directory into your Downloads directory (if it is downloaded by default). 
Untar the folder called "IDLSave-1.0.0.tar.gz"
CD into the directory and type: 
                    python setup.py install 


 This should install the package. 

Note that you can also get the package using:

                    pip install idlsave

Open a terminal where you have a .sav file and start python. 

Python 2.7.5 (v2.7.5:ab05e7dd2788, May 13 2013, 13:18:45)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import idlsave
>>> s = idlsave.read('all_mdwarfs.sav')

--------------------------------------------------
Date: Thu May  3 20:47:14 2012
User: ryan
Host: HPC
--------------------------------------------------
Format: 10
Architecture: x86_64
Operating System: darwin
IDL Version: 8.0
--------------------------------------------------
Successfully read 5 records of which:
 - 1 are of type VARIABLE
 - 1 are of type TIMESTAMP
 - 1 are of type NOTICE
 - 1 are of type VERSION
--------------------------------------------------
Available variables:
 - all [<class 'numpy.core.records.recarray'>]
--------------------------------------------------
Note that in this case the variable is called 'all'. This .sav file is a structure. You might get a bunch of errors. Have a look at those and decide if you can ignore them. In most cases you can. 

Now if I do: 

>>> s.all.dtype
dtype([(('name', 'NAME'), '|O8'), (('ra', 'RA'), '>f8'), (('de', 'DE'), '>f8'), (('_2mass', '_2MASS'), '|O8'), (('pmra', 'PMRA'), '>f8'), (('pmde', 'PMDE'), '>f8'), (('vmag', 'VMAG'), '>f8'), (('jmag', 'JMAG'), '>f8'), (('hmag', 'HMAG'), '>f8'), (('kmag', 'KMAG'), '>f8'), (('v_j', 'V_J'), '>f8'), (('visits', 'VISITS'), '>f8'), (('field', 'FIELD'), '|O8'), (('origin', 'ORIGIN'), '>i2'), (('proper_motion_src', 'PROPER_MOTION_SRC'), '|O8'), (('priority', 'PRIORITY'), '>i2'), (('type', 'TYPE'), '|O8'), (('ra2mass', 'RA2MASS'), '>f8'), (('de2mass', 'DE2MASS'), '>f8')])


I get the structure or the headers for each of the columns. Now you can parse each column. For example, I can parse just the RA as: 

>>> ra = s.all.ra

That's it. You have now read and parsed IDL .sav file without running IDL! 