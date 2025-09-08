# Advance Prompting Techniques

## **1. Introduction**
Recently, Artificial Intelligence has boosted in the world IT sector. As more advancements are being made in AI, the need for advanced prompting techniques to get more accurate results has never been higher. This article examines various prompting techniques applied to an LLM model to evaluate their effect on its performance.

## **2. Techniques**
Following techniques are used in prompting :-

- Zero-Shot → no examples, direct instruction.  
- Few-Shot → include examples.   
- Chain of Thought (CoT) → explicitly ask the model to “think step by step”   

## **3. Tasks for Evaluation**  

**Task-1 : Reasoning Task** --> If it is raining, the ground will be wet. The ground is wet. Does it mean it rained?  
**Task-2 : Logic Puzzles** --> Alice is older than Bob. Bob is older than Charlie. Who is the youngest?<br>
**Task-3 : Math Problems** --> If a pizza is cut into 8 equal slices and you eat 3, what fraction remains?  

## **4. Model Evaluated**
DeepSeek-R1 (free) is an open-source large language model with a Mixture-of-Experts architecture, supporting up to 128K tokens. It is optimized for reasoning, math, and coding tasks, offering performance comparable to top models at lower cost, and is freely available under the MIT license.

## **5. Record Outputs** 

## Task-1: Reasoning Task--> If it is raining, the ground will be wet. The ground is wet. Does it mean it rained?

- **Zero-Shot**
  - Output: The conclusion that "it rained" does not necessarily follow from the premises given. This is an example of the logical fallacy called affirming the consequent

- **Few-Shot**
  - Output: Not necessarily. The ground being wet could be due to other reasons, such as a sprinkler being on or someone spilling water. The original statement only confirms that rain leads to wet ground, not that rain is the only cause.

- **Chain-of-Thought**
  - Output: The original statement establishes a logical relationship:  
  If it is raining (A), then the ground will be wet (B). This is written as A → B.  Observing that the ground is wet (B) only confirms the consequent of the implication. However, A → B does NOT mean B → A. Assuming the converse (B → A) is a logical fallacy called affirming the consequent. The wet ground could have alternative causes (e.g., a sprinkler, spilled water, melting snow), so B being true does not guarantee A is true.  
  **Conclusion**: The wet ground suggests rain as a possible explanation, but it does not prove it rained. Logical certainty requires additional evidence.


## Task 2: Logic Puzzles --> Alice is older than Bob. Bob is older than Charlie. Who is the youngest? 

- **Zero-Shot**
  - Output: The youngest person is Charlie.

- **Few-Shot**
  - Output: Charlie is the youngest. 

- **Chain-of-Thought**
  - Output: Given Relationships:  
    Alice > Bob (Alice is older than Bob).  
Bob > Charlie (Bob is older than Charlie).  
Apply Transitivity:
Combining these: Alice > Bob > Charlie.  
**Conclusion:** Charlie is the youngest in the sequence

## Task 3: Math Problems → If a pizza is cut into 8 equal slices and you eat 3, what fraction remains?

- **Zero-Shot**  
  - Output: The pizza has 8 slices. If 3 are eaten, 5 remain. The fraction left is 5/8.  

- **Few-Shot**  
  - Output: A whole pizza has 8 slices. Eating 3 leaves 5. The remaining part is represented as 5 out of 8 slices, so the fraction is 5/8.  

- **Chain-of-Thought**  
  - Output: The problem states the pizza is divided into 8 equal slices. Eating 3 slices means we subtract 3 from 8, leaving 5 slices. Since fractions represent “part over whole,” the remaining portion is 5 (remaining slices) over 8 (total slices).  
  **Conclusion**: The fraction of the pizza that remains is **5/8**.  

## **6. Comparison of Prompting Techniques** 

- **Zero shot** : Results driven from zero shot were accurate and brief but lacked context as in Task-1 it gave the correct logic fallacy but lacked elaboration.<br><br>
- **Few Shot**  : Contextuat Accuracy was improved by giving relatable explanations and alternative possibilities. The presence of examples helped the model generalize reasoning patterns better as in Task-1 it mentioned sprinklers and other causes of wet ground.<br><br>
- **Chain of Thought** : consistently offered the most structured reasoning. It explained the logical or mathematical process step by step, clearly showing how conclusions were derived: <br> Task-1 formalized A → B logic <br> Task-2 demonstrated transitivity <br> Task-3 explained fractions thoroughly.<br> This makes CoT the most reliable when transparency and reasoning quality are required. 

## **7. Evaluation of Prompting Techniques**

| Technique   | Correctness (0–3) | Reasoning Clarity <br>(0–3) | Completeness (0–3) | Conciseness (0–3) | Total (12) |
|-------------|-------------------|--------------------------|---------------------|-------------------|------------|
| Zero-Shot   | 3                 | 1                        | 1                   | 3                 | **8**      |
| Few-Shot    | 3                 | 2                        | 2                   | 2                 | **9**      |
| CoT         | 3                 | 3                        | 3                   | 2                 | **11**     |

## **8. Conclusion** 
- For quick and direct answers → Zero-Shot is sufficient.<br>
- For context-rich but concise responses → Few-Shot works best.<br>
- For detailed reasoning, logical transparency, and academic rigor → CoT outperforms the others

Hence, after testing the following methods on various prompts Chain of Thought (CoT) achieved the highest score, demonstrating the most complete and accurate reasoning compared to the other techniques. 

