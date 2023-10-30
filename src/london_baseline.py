# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from run import evaluate_places

path = "../birth_dev.tsv"

with open(path) as fin:
    lines = len([x.strip().split('\t') for x in fin])

evaluate_places(path, ['London'] * lines)
