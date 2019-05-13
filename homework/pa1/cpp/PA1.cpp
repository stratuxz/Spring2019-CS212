/*
 Zahory Velazquez
 012896205
 05.06.2019
*/

#include "PA1.h"

//PA #1 TOOD: Generates a Huffman character tree from the supplied text
HuffmanTree<char>* PA1::huffmanTreeFromText(vector<string> data)
{

    //Builds a Huffman Tree from the supplied vector of strings.
    //This function implement's Huffman's Algorithm as specified in the
    //book.

    //In order for your tree to be the same as mine, you must take care 
    //to do the following:
    //1.	When merging the two smallest subtrees, make sure to place the 
    //      smallest tree on the left side!
	
   //store frequencies in hashtable
   unordered_map<char, int>frequencies{};
   
   // xcode was warning of int so I changed to unsigned long (doesnt really make a diff)
   for(unsigned long i = data.size()-1; 0 <= i; i--) // start from the end so we can pop
   {
      string word = data[i];
      
      for (char character : word)
      {
         frequencies[character]++;
      }
      data.pop_back(); // pop element off
   }
   
   //maintains huffman tree forest
   priority_queue < HuffmanTree<char>*, vector<HuffmanTree<char>*>, TreeComparer> forest{};
   
   for(auto kvp : frequencies)
   {
      // the beginning of a tree - all start as leaf nodes
      HuffmanTree<char>* character = new HuffmanTree<char>(kvp.first, kvp.second);
      forest.push(character);
   }
   
   while(forest.size() > 1) // continuosly merge till one tree
   {
      HuffmanTree<char>* left = forest.top();
      forest.pop();
      
      HuffmanTree<char>* right = forest.top();
      forest.pop();
      
      HuffmanTree<char>* merge = new HuffmanTree<char>(left,right);
      
      forest.push(merge);
      
   }
   
    //TODO: shouldn't return nullptr
    return forest.top();
}

//PA #1 TODO: Generates a Huffman character tree from the supplied encoding map
//NOTE: I used a recursive helper function to solve this!
HuffmanTree<char>* PA1::huffmanTreeFromMap(unordered_map<char, string> huffmanMap)
{
	HuffmanNode<char>* root = new HuffmanInternalNode<char>{ nullptr, nullptr };
   // convert data type
	HuffmanInternalNode<char>* current = dynamic_cast<HuffmanInternalNode<char>*>(root);
   
   for (auto kvp : huffmanMap)
   {
      string path = kvp.second;
      char value = kvp.first;
      
      for (int i = 0; i < path.length() - 1; i++)
      {
         char ch = path[i];
         if (ch == '0')
         {
            //left
            if (current->getLeftChild() == nullptr)
            {
               current->setLeftChild(new HuffmanInternalNode<char>{ nullptr, nullptr });
            }
            current = dynamic_cast<HuffmanInternalNode<char>*>(current->getLeftChild());
         }
         else
         {
            //right
            if (current->getRightChild() == nullptr)
            {
               current->setRightChild(new HuffmanInternalNode<char>{ nullptr, nullptr });
            }
            current = dynamic_cast<HuffmanInternalNode<char>*>(current->getRightChild());
         }
         
      }
      
      char last_ch = path[path.length() - 1];
      if (last_ch == '0')
      {
         current->setLeftChild(new HuffmanLeafNode<char>{ value, 0 });
      }
      else
      {
         current->setRightChild(new HuffmanLeafNode<char>{ value, 1 });
      }
   }
    //Generates a Huffman Tree based on the supplied Huffman Map.Recall that a
    //Huffman Map contains a series of codes(e.g. 'a' = > 001).Each digit(0, 1) 
    //in a given code corresponds to a left branch for 0 and right branch for 1.
   
   HuffmanTree<char>* tree = new HuffmanTree<char>(current); // create tree
   
    return tree;
}

//PA #1 TODO: Generates a Huffman encoding map from the supplied Huffman tree
//NOTE: I used a recursive helper function to solve this!

void encodingHelper(unordered_map<char, string>& huffmanMap, HuffmanNode<char>* node, string path = "")
{
   if(node->isLeaf() == true) // check if its leaf
   {
      // convert from HuffmanNode to HuffmanLeafNode
      HuffmanLeafNode<char> *leaf = dynamic_cast<HuffmanLeafNode<char>*>(node);
      char value = leaf->getValue();
      
      huffmanMap[value] = path;
      
      return;
   }
   else // if not leaf, then internal
   {
      HuffmanInternalNode<char>* internal = dynamic_cast<HuffmanInternalNode<char>*>(node);
      
      encodingHelper(huffmanMap, internal->getLeftChild(), path + '0'); // left add 0
      encodingHelper(huffmanMap, internal->getRightChild(), path + '1'); // right add 1
      
   }
}

unordered_map<char, string> PA1::huffmanEncodingMapFromTree(HuffmanTree<char> *tree)
{
	HuffmanNode<char> *node = tree->getRoot();
	if (node->isLeaf() == true)
	{
		HuffmanLeafNode<char> *leaf = dynamic_cast<HuffmanLeafNode<char>*>(node);
		leaf = (HuffmanLeafNode<char> *)node;
	}

    //Generates a Huffman Map based on the supplied Huffman Tree.  Again, recall 
    //that a Huffman Map contains a series of codes(e.g. 'a' = > 001).Each digit(0, 1) 
    //in a given code corresponds to a left branch for 0 and right branch for 1.  
    //As such, a given code represents a pre-order traversal of that bit of the 
    //tree.  I used recursion to solve this problem.
    unordered_map<char, string> result{};
   
   encodingHelper(result, tree->getRoot());
   
    return result;
}

//PA #1 TODO: Writes an encoding map to file.  Needed for decompression.
void PA1::writeEncodingMapToFile(unordered_map<char, string> huffmanMap, string file_name)
{
    //Writes the supplied encoding map to a file.  My map file has one 
    //association per line (e.g. 'a' and 001 would yield the line "a001")
   ofstream write(file_name);
   // write charpath\n
   for(auto kvp : huffmanMap)
   {
      write << kvp.first << kvp.second << endl;
   }
   write.close();
}

//PA #1 TODO: Reads an encoding map from a file.  Needed for decompression.
unordered_map<char, string> PA1::readEncodingMapFromFile(string file_name)
{
    //Creates a Huffman Map from the supplied file.Essentially, this is the 
    //inverse of writeEncodingMapToFile.
   unordered_map<char, string> result{};
   
   ifstream read(file_name);
   
   if(read.is_open())
   {
      string line = "";
      // go through every line in file
      while(getline(read, line))
      {
         string path = "";
         char value;
         // everyline should have valuepath (eg. a001)
         // go through every char in line
         for(int i = 0; i < line.size(); i++)
         {
            if(i == 0)
            {
               value = line[i]; // first char should be a character (e.g a)
            }
            else
            {
               path += line[i]; // rest chars are path (e.g 001)
            }
         }
         result[value] = path;
      }
   }
   
   read.close();
   
   return result;
}

//PA #1 TODO: Converts a vector of bits (bool) back into readable text using the supplied Huffman map
string PA1::decodeBits(vector<bool> bits, unordered_map<char, string> huffmanMap)
{
    //Uses the supplied Huffman Map to convert the vector of bools (bits) back into text.
    //To solve this problem, I converted the Huffman Map into a Huffman Tree and used 
    //tree traversals to convert the bits back into text.
    ostringstream result{};
   // convert map to tree
   HuffmanTree<char>* tree = huffmanTreeFromMap(huffmanMap);
   
   // assign nodes to leaf or internal
   HuffmanInternalNode<char>* internal_node = dynamic_cast<HuffmanInternalNode<char>*>(tree->getRoot());
   HuffmanLeafNode<char>* leaf_node = dynamic_cast<HuffmanLeafNode<char>*>(tree->getRoot());
   
   for(int i = 0; i < bits.size(); i++)
   {
      if(bits[i] == 0) // if first is 0
      {
         // left node
         HuffmanNode<char>* left = internal_node->getLeftChild();
         
         if(internal_node->getLeftChild()->isLeaf() == false) // if internal
         {
            internal_node = dynamic_cast<HuffmanInternalNode<char>*>(left);
         }
         else // if leaf
         {
            leaf_node = dynamic_cast<HuffmanLeafNode<char>*>(left);
            result << leaf_node->getValue();
            
            // make sure to go back to root when a leaf node is reached
            internal_node = dynamic_cast<HuffmanInternalNode<char>*>(tree->getRoot());
         }
      }
      else
      {
         HuffmanNode<char>* right = internal_node->getRightChild();
         
         if(internal_node->getRightChild()->isLeaf() == false) // if interal
         {
            internal_node = dynamic_cast<HuffmanInternalNode<char>*>(right);
         }
         else // if leaf
         {
            leaf_node = dynamic_cast<HuffmanLeafNode<char>*>(right);
            result << leaf_node->getValue();
            
            // make sure to go back to root when a leaf node is reached
            internal_node = dynamic_cast<HuffmanInternalNode<char>*>(tree->getRoot());
         }
      }
   }
   
    return result.str();
}

//PA #1 TODO: Using the supplied Huffman map compression, converts the supplied text into a series of bits (boolean values)
vector<bool> PA1::toBinary(vector<string> text, unordered_map<char, string> huffmanMap)
{
   vector<bool> result{};
   
   for(string word : text)
   {
      for (char character : word)
      {
         auto search = huffmanMap.find(character);
         if(search != huffmanMap.end()) // find character in map
         {
            bool data;
            istringstream(search->second) >> data; // convert path to bool
            result.push_back(data);
         }
      }
   }
   return result;
}
