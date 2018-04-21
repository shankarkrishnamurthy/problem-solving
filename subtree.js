/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
};

/**
 * @param {TreeNode} s
 * @param {TreeNode} t
 * @return {boolean}
 */
var isSubtree = function(s, t) {
    function is_valid(a,b) {
        if (!a && !b) { return true; }
        if (!a || !b || a.val !== b.val) { return false; }

        return is_valid(a.left, b.left) && is_valid(a.right, b.right);
    };
    
    function do_subtree(x,y) {
        console.log("Enter " + x + " " + y);
        if (is_valid(x,y)) {
            console.log("IS TRUE " + x + " " + y);
            return true;
        } else {
            if (!x) return false;
            return do_subtree(x.left, y) || do_subtree(x.right, y);
        }
    };
    return do_subtree(s,t);
};

console.log(isSubtree(null, null));
console.log(isSubtree(new TreeNode(1), null));
console.log(isSubtree(null, new TreeNode(1)));
console.log(isSubtree(new TreeNode(1),new TreeNode(3)));
var s = new TreeNode(1); s.left = new TreeNode(5); s.left.left = new TreeNode(2);//s.left.left.left=new TreeNode(0);
var t = new TreeNode(5);t.left = new TreeNode(2);
console.log(isSubtree(s,t));
