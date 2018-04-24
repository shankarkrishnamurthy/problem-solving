function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var diameterOfBinaryTree = function(root) {
    var msf=0;
    if (!root) { return 0; }
    function do_dbt(root) {
        if (!root) { return 0;}
        var ldia = do_dbt(root.left);
        var rdia = do_dbt(root.right);
        msf = Math.max(msf, ldia + rdia + 1);
        return Math.max(ldia, rdia) + 1;
    }
    do_dbt(root);    
    return msf-1;
};

r = new TreeNode(3);
console.log(diameterOfBinaryTree(r));
