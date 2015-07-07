import sys
import operator

# High recall, low precision.
def check_profane_content_by_substrings(line, explicit_words):
    for explicit_word in explicit_words:
        if explicit_word in line:
            # print '%s found in %s' % (explicit_word, line)
            return True
    return False

# Low recall, high precision
def check_profane_content_by_word_splits(line, explicit_words):
    word_set = set(line.split(' '))
    for explicit_word in explicit_words:
        if explicit_word in word_set:
            # print '%s found in %s' % (explicit_word, line)
            return True
        explicit_phrase_set = explicit_word.split(' ')
        has_all = True
        for epm in explicit_phrase_set:
            if epm not in word_set:
                has_all = False
        if has_all:
            # print '%s (phrase) found in %s' % (explicit_word, line)
            return True
    return False;

def profane_content(line, explicit_words, check_substrings=True):
    punctuation_set = ['.', '-', '_', '"', ',']
    for p in punctuation_set:
        line = line.replace(p, ' ')

    if check_substrings:
        return check_profane_content_by_substrings(line, explicit_words)
    else:
        return check_profane_content_by_word_splits(line, explicit_words)

def check_word_stats(wdict, line):
    for x in map(lambda(x): x.lower(), line.split(' ')):
	    wdict[x] = wdict.get(x, 0) + 1
    return wdict

def main(argv):
    if len(argv) != 2:
        print 'Usage: python process_list.py <list-to-process> <explicit-word-list>'
        sys.exit(1)

    file_to_process = argv[0]
    lines = open(file_to_process).read().splitlines()

    explicit_words_file = argv[1]
    explicit_words = set(open(explicit_words_file).read().splitlines())

    splits = []
    for l in lines:
        splits.append(l.split('\t'))

    profane_splits = []
    not_profane_splits = []
    use_substrings = False
    wdict = {}

    profane_pages_file = open(file_to_process + '.porny', 'w+')
    regular_pages_file = open(file_to_process + '.regular', 'w+')
    for split in splits:
        if profane_content(split[0].lower(), explicit_words, use_substrings):
            profane_splits.append(split)
            profane_pages_file.write("{}\n".format(split[0]))
        else:
            not_profane_splits.append(split)
            regular_pages_file.write("{}\n".format(split[0]))
            wdict = check_word_stats(wdict, split[0])

    profane_pages_file.close()
    regular_pages_file.close()

    print('Total: %d'  % (len(profane_splits) + len(not_profane_splits)))
    print('Number of Porny Sentences: %d' % (len(profane_splits)))
    print('Number of Regular Sentences: %d' % (len(not_profane_splits)))

    # Uncomment below, to see the top 200 words along with their frequency,
    # which the classifier marked to be fine. Adjust the corpus accordingly.
    #sorted_list = sorted(wdict.items(), key=operator.itemgetter(1))[::-1][0:200]
    #print sorted_list

if __name__ == "__main__":
    main(sys.argv[1:])
