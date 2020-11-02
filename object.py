# -*- coding: utf-8 -*-

# Copyright (C) 2020 Botir Ziyatov <botirziyatov@gmail.com>
# This program is free software: you can redistribute it and/or modify

from typing import Dict, List
import requests


API_LINK = "http://87.237.234.204:7456/back/v2/GetExchangeCourses/1"

updates = requests.get(API_LINK).json()

ien = updates[21]['rate']
frank = updates[47]['rate']
sterling = updates[55]['rate']
dollar = updates[56]['rate']
evro = updates[74]['rate']
rubl = updates[41]['rate']

