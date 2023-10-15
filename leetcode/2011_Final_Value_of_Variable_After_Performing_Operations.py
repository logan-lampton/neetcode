class Solution:
    def finalValueAfterOperations(self, operations: [str]) -> int:
        x = 0

        op_hash = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }

        for op in operations:
            # checking if the op is in the op_hash saves a lot of runtime
            if op in op_hash:
                x += op_hash[op]
        return x
