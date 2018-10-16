from neo4j.v1 import GraphDatabase
import string

driver = GraphDatabase.driver(
            "bolt://0.0.0.0:7689",
            auth=("neo4j", "K1r0ku"))


note_stack = []
with open("dbStore.txt") as notes:
    for note in notes:
        tmp_note_list = note.rstrip().replace(',', '').split(" ")
        note_stack.append(tmp_note_list)


def add_notes_to_db_from_note_stack(stack):
    stack_len = stack.__len__()
    stack_indx = 0

    grab_note_from_top_of_stack(stack, stack_indx, stack_len)
    return 'stack is empty'


def grab_note_from_top_of_stack(stack, index, length):
    if index == length:
        return 'no more notes'

    retrieve_words_from_note(stack[index])

    return grab_note_from_top_of_stack(stack, index+1, length)


def retrieve_words_from_note(note):
    # note_len = note.__len__()
    # note_indx = 0

    # def words(note, note_indx, note_len):
    #     if note_indx == note_len:
    #         return 1

    #     return words(note, note_indx+1, note_len)

    #     print(note[note_indx])

    # words(note, note_indx, note_len)


def add_word_to_db(word):
    print(word)

def word_relationship(current_word, prev_word):
    return word_relationship(word, word)

if __name__ == '__main__':
    print(add_notes_to_db_from_note_stack(note_stack))