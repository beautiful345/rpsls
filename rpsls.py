#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021/06/04
"""

import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
	    name=0
    elif name=="ʷ����":
	    name=1
    elif name=="��":
	    name=2
    elif name=="����":
	    name=3
    else:
        name=4
    return name 
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
	    return"ʯͷ"
    elif number==1:
	    return"ʷ����"
    elif number==2:
	    return"��"
    elif number==3:
	    return"����"
    elif number==4:
	    return"����"	
    else:
        return"��������"
def rpsls(name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    
# �Գ�����в���
rpsls
#rpsls("lizard")
print("--------")
name=input("����������ѡ��:")
print("--------")
playerchoice=name_to_number(name)
print("����ѡ��Ϊ:")
computerchoice=random.randrange(0,4)
print("�������ѡ��Ϊ:"+number_to_name(computerchoice))
diff=(playerchoice-computerchoice)%5
if (diff==1)or(diff==2):
	print("��Ӯ�ˣ�")
elif (diff==3)or(diff==4):
	print("����Ӯ��")
else:
	print("���ͼ��������һ����")

