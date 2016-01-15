#!/usr/bin/env python
# filename: pipeline.py


#
# Copyright (c) 2015 Bryan Briney
# License: The MIT license (http://opensource.org/licenses/MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import glob
import os

from abtools import log


def initialize(log_file, project_dir=None, debug=False):
	_print_splash()
	log.setup_logging(log_file, print_log_location=False, debug=debug)
	logger = log.get_logger('pipeline')
	if project_dir is not None:
		logger.info('PROJECT DIRECTORY: {}'.format(project_dir))
		logger.info('')
	logger.info('LOG LOCATION: {}'.format(log_file))
	print('')
	return logger


def make_dir(d):
	if not os.path.exists(d):
		os.makedirs(d)


def list_files(d):
	if os.path.isdir(d):
		expanded_dir = os.path.expanduser(d)
		files = sorted(glob.glob(expanded_dir + '/*'))
	else:
		files = [d, ]
	return files


def _print_splash():
	splash = '''     _    _   _____           _       ____  _            _ _            
    / \  | |_|_   _|__   ___ | |___  |  _ \(_)_ __   ___| (_)_ __   ___ 
   / _ \ | '_ \| |/ _ \ / _ \| / __| | |_) | | '_ \ / _ \ | | '_ \ / _ \\
  / ___ \| |_) | | (_) | (_) | \__ \ |  __/| | |_) |  __/ | | | | |  __/
 /_/   \_\_.__/|_|\___/ \___/|_|___/ |_|   |_| .__/ \___|_|_|_| |_|\___|
                                             |_|                        '''
	print('')
	print(splash)
	print('')