import xml.etree.ElementTree
from argparse import ArgumentParser
def init_parser():
  parser = ArgumentParser()
  parser.add_argument('--FEMB', type=int, help='FEMB in stream', default=3)
  parser.add_argument('--input', type=str, help='Input File', default='femb_stream0.txt')
  parser.add_argument('--output', type=str, help='Output Directory', default='')
  return parser

#print a.config

