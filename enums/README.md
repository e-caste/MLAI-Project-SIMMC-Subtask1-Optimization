## Enumarators for target Action/Attribute
The two classes contains the possible values of actions or attributes that model can predict.
- `"action"`: the possible action are:
  (`None, SpecifyInfo, AddToChart, SearchInMemory, SearchInDatabase`)
    
- `"attributes"` the possible values of attributes are:
  (`color, price, info, customeRating, brand, pattern, embellishment, hemlength, availableSizes`)
  - `other` represent another possible value, and convert all attributes not included in previous list
    
Action/Attribute class contains this methods:
```
    def from_str(cls, string):
    ...
    
    def _from_number(cls, number):
    ...
    
  ```

- `from_str` : convert a string in enum value
- `from_number` : convert a enum value (integer) in string