import os
from pathlib import Path
from envs import CONTENT_PATH

def load_md_files():
  topics_file = CONTENT_PATH + "/topics"
  md_files = []
  for subdir, _, files in os.walk(topics_file):
    for file in files:
      filepath = subdir + os.sep + file
      if filepath.endswith(".md"):
        md_files.append(filepath)
  return md_files

MD_FILES = load_md_files()

def test_one_question_separator():
  for file in MD_FILES:
     file_text = Path(file).read_text()
     separators_count = file_text.count("?---?")
     assert separators_count < 2, "There can be only one questions separator in lesson's markdown. File path: " + file

parser = commonmark.Parser()

HEADING = 'heading'
LIST = 'list'

def test_answer_count():
  for file in MD_FILES:
    file_text = Path(file).read_text()
    separators_count = file_text.count("?---?")
    if separators_count == 1:
      questions_section = file_text.split("?---?", 1)[1]
      ast = parser.parse(questions_section)
      elem = ast.first_child
      print("FILE: " + file)
      print(commonmark.dumpAST(ast))
      assert elem.t == HEADING, "First element in question section has to be a heading. File path: " + file 

      # print("--- SEP ---")
      # while elem != None:
      #   pprint(vars(elem))
      #   if elem.t == LIST:
      #     point = elem.first_child
      #     isMulti = False
      #     while point != None:  
      #       print("  - Point:")
      #       pprint(vars(point))
      #       pprint(vars(point.first_child.first_child))
      #       point = point.nxt
      #   print("- next -")
      #   elem = elem.nxt
