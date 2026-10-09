/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    
    if (p === null && q === null) return true;
    if (p === null || q === null) return false;

    if(p.val !== q.val) return false;

    let ret = true;

    if((p.left !== null) == (q.left !== null)) {
        ret = ret && isSameTree(p.left, q.left)
    } else {
        ret = false;
    }

    if((p.right !== null) == (q.right !== null)) {
        ret = ret && isSameTree(p.right, q.right)
    } else {
        ret = false;
    }

    return ret;
};