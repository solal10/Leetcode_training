/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function(root) {
    if (!root) return 0; // Edge case: empty tree

    let leftHeight = getHeight(root.left);
    let rightHeight = getHeight(root.right);

    if (leftHeight === rightHeight) {
        // Left subtree is a full tree of height `leftHeight`
        return (1 << leftHeight) + countNodes(root.right);
    } else {
        // Right subtree is a full tree of height `rightHeight`
        return (1 << rightHeight) + countNodes(root.left);
    }
};

/**
 * Helper function to get the height of the tree
 */
function getHeight(node) {
    let height = 0;
    while (node) {
        height++;
        node = node.left; // Move down to count levels
    }
    return height;
}