class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]
        
        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j] 
                
        return image
