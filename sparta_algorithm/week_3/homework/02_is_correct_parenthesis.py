s = "(())()("


def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []

    for i in range(len(string)):
        if string[i] == '(':    # 문자열에 있는 '('를 스택에 추가
            stack.append('(')
        else:
            if len(stack) is None:  # '('이 없어 스택이 비어있다면
                return False        # 닫힌 괄호가 먼저 나와 올바른 괄호가 아니므로 False 반환
            stack.pop()     # 성공적으로 괄호를 닫았다면 스택에서 '(' 한개를 제거

    if len(stack) == 0:  # 스택이 비어 있다면 모든 괄호가 성공적으로 닫힌 것이므로 True 반환
        return True
    else:
        return False    # 스택이 비어 있지 않다면 열린 괄호가 남아있는 것이므로 False 반환


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
