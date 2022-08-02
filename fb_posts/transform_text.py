import os
import re
current_dir = os.path.dirname(__file__) 
fb_posts_filepath = f'{current_dir}\\fb_posts.md'

with open(fb_posts_filepath, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    number_of_posts = 0

    for line_number, line_text in enumerate(lines, 1):
      line_begins_with_date = re.match('\d{1,2}\.\d{1,2}\.\d{4}', line_text)
      if (line_begins_with_date):
        number_of_posts += 1

    current_post_number = 0;
    updated_lines = []

    for line_number, line_text in enumerate(lines, 1):
      line_begins_with_date = re.match('\d{1,2}\.\d{1,2}\.\d{4}', line_text)
      if (line_begins_with_date):
        date_string = line_begins_with_date.string
        date_string = date_string.rstrip('\n')
        post_id_number = number_of_posts - current_post_number
        current_post_number += 1
        line_index = line_number - 1
        post_id_string = f'post_id_{post_id_number}' 
        lines[line_index]= f'### [{date_string} Пост-{post_id_number}](/blog/facebook-postove#{post_id_string}) <a id="{post_id_string}"></a>\n'

      # updated_lines.append(line_text)

with open('fb_posts_edited.md', 'w', encoding='utf-8') as file:
    file.writelines(lines)