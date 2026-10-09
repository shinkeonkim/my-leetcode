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

    return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

function mirrorTree(p: TreeNode | null): TreeNode {
    if(p === null) return p;

    let left = mirrorTree(p.left);
    let right = mirrorTree(p.right);

    p.left = right;
    p.right = left;

    return p;
}

function isSymmetric(root: TreeNode | null): boolean {
    if(root === null) return true;

    return isSameTree(root.left, mirrorTree(root.right));
};