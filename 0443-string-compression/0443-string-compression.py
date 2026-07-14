class Solution:
    def compress(self, chars: List[str]) -> int:
        stack =[]
        i=0
        while i < len(chars):
            count =0 
            ch = chars[i]
            while i<len(chars) and chars[i]==ch :
                i+=1
                count+=1
            stack.append(ch)
            if count > 1:
                stack.extend(str(count))
        for j in range(len(stack)):
            chars[j] = stack[j]
        return len(stack)