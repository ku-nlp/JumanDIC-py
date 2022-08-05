# https://github.com/ku-nlp/jumanpp/blob/master/script/sexp.py
import re

re_word = re.compile(r'^("(?:[^"\\]+|\\.)*")')
re_symbol = re.compile(r'^([^\s"()]+)')


def parse(input_text):
    texts = input_text.split("\n")
    string = ""
    stack = []
    offsets = []
    text_itr = iter(texts)
    while True:
        string = string.lstrip()
        if string.startswith(";"):
            # 行を飛ばす
            string = ""  # 複数行の入力は無い
        if len(string) == 0:
            try:
                string = next(text_itr)
            except StopIteration:
                if len(offsets) > 0:
                    raise Exception("Syntax error: end of target during parsing.")
                else:
                    break
        elif string.startswith("("):
            string = string[1:]
            if len(offsets) > 0:
                offsets[0] -= 1
            offsets.insert(0, 0)
        elif string.startswith('"'):
            while True:
                match = re_word.search(string)
                if match:
                    offsets[0] -= 1
                    stack.append(match.group(1))
                    string = string[len(match.group(1)) :]
                    break
                else:
                    try:
                        string += next(text_itr)
                    except StopIteration:
                        raise Exception("Syntax error: end of target during string.")
        elif re_symbol.search(string):
            match = re_symbol.search(string)
            offsets[0] -= 1
            stack.append(match.group(1))
            string = string[len(match.group(1)) :]
        elif string.startswith(")"):
            string = string[1:]
            if not (len(offsets) > 0):
                raise Exception("Syntax error: too much close brackets.")
            else:
                offset = offsets.pop(0)
                if offset < 0:
                    sl = stack[offset:]
                    del stack[offset:]
                    stack.append(sl)
                else:
                    stack.append([])
        else:
            raise Exception("Syntax error: unknown syntax element.")
    return stack


def is_empty_line(line: str) -> bool:
    if line.strip() == "":
        return True
    if line.startswith(";"):
        return True
    return False
