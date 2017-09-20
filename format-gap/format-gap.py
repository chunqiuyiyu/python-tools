import sublime, sublime_plugin
import re

class FormatGapCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    word = self.view.find_all(r'[a-zA-Z0-9]+')
    offset = 0

    if word:
      for item in word:
        # Insert left space
        index = item.begin()
        flag = re.match(u"[\u4e00-\u9fa5]", self.view.substr(index + offset - 1))
        if flag:
          self.view.insert(edit, index + offset, ' ')
          # Because the current view is changed by inserting space
          # we should add the offset to get correct position
          offset = offset + 1

        # Insert right space
        index = item.end()
        index = index + offset
        flag = re.match(u"[\u4e00-\u9fa5]", self.view.substr(index))
        if flag:
          self.view.insert(edit, index, ' ')
          offset = offset + 1

  # We only need 'Format Gap' in Markdown file
  def is_enabled(self):
    name = self.view.file_name()
    if name[-2:] == 'md':
      return True
    else:
      return False
