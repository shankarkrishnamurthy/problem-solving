func permute(nums []int) [][]int {
    res:=make([][]int,0)
    n:=len(nums)
    var backTrack func(int)
    backTrack=func(first int){
        if first == n{
            temp:=make([]int, n)
            copy(temp,nums)
            res = append(res, temp)
        }
        for i:=first;i<n;i++{
            nums[first],nums[i] = nums[i],nums[first]
            backTrack(first+1)
            nums[first],nums[i] = nums[i],nums[first]
        }
    }
    backTrack(0)
    return res
}

func max(a,b int) int { if a > b { return a} else { return b} }

func maxCompatibilitySum(stud [][]int, men [][]int) (res int) {
    m, n, lobj, rc:= len(men), len(men[0]), make([]int, len(men)), 0
    cs, b2i := make([][]int, m), map[bool]int{false: 0, true: 1}
    for i := range cs { cs[i] = make([]int, m) }
    for i:=0; i < m; i++ {
        for j:=0; j< m; j++ {
            for k:=0; k< n; k++ {
                cs[i][j] += b2i[men[j][k] == stud[i][k]]
            } 
        }
        lobj[i] = i
    }
    for _, r := range permute(lobj) {
        rc = 0
        for i,v := range r { rc += cs[i][v] }
        res = max(res, rc)
    }
    
    //fmt.Println(b2i, cs, m, n)
    return res
}
