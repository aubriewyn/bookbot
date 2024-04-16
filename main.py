def main():
  file_path = 'books/frankenstein.txt'
  with open(file_path) as f:
    file_contents = f.read()
    count = word_count(file_contents)
    print(f'--- Begin report of {file_path} ---')
    print(f"{count} Words found in the document\n")
    for letter in convert_to_sorted_list(create_letters_dict(file_contents)):
      if letter['letter'].isalpha():
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print('--- End report ---')


def word_count(string):
  return len(string.split())


def create_letters_dict(string):
  letters = {}
  for s in string.lower():
    if s in letters:
      letters[s] += 1
    else:
      letters[s] = 1

  return letters


def convert_to_sorted_list(dict):
  new_list = []
  for key, value in dict.items():
    new_list.append ({'letter': key, 'count': value})
  new_list.sort(reverse=True, key=sort_on)
  return new_list



def sort_on(dict):
  return dict['count']


main()
