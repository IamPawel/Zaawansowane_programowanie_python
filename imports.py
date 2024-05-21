import cv2 as cv
import numpy as np
import requests
import time
import os
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify
import uuid
import json
import pika
import base64
