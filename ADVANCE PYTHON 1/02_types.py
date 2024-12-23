from typing import List,Tuple,Dict,Union

numbers: List[int] = [1,2,3,4,5]

person: Tuple[str,int] = ("Alice",30)

scores:  Dict[str,int] = {"Alice":90,"Bob":87}

identifier: Union[int,str] = "ID123"
identifier = 12345

print(numbers,person,scores,identifier)