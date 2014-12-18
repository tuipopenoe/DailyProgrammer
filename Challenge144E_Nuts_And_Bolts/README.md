## Description
You have just been hired at a local home improvement store to help compute the proper costs of inventory. The current prices are out of date and wrong; you have to figure out which items need to be re-labeled with the correct price.
You will be first given a list of item-names and their current price. You will then be given another list of the same item-names but with the correct price. You must then print a list of items that have changed, and by how much.

### Input
The first line of input will be an integer N, which is for the number of rows in each list. Each list has N-lines of two space-delimited strings: the first string will be the unique item name (without spaces), the second string will be the price (in whole-integer cents). The second list, following the same format, will have the same unique item-names, but with the correct price. Note that the lists may not be in the same order!


### Output
For each item that has had its price changed, print a row with the item name and the price difference (in cents). Print the sign of the change (e.g. '+' for a growth in price, or '-' for a loss in price). Order does not matter for output.