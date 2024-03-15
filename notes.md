## Notes



### Doing OG in photoshop


Detail layers can be imported using the **UG tool > Import from detail**, as `Overgrowth.raw` and  `Undergrowth.raw` are interchangeable.
Each detail map channel is converted to UG types, as follows:

Primary layers (`tx*_1.dds`)
| Code | Color | UG mode color | Used for
| --- | --- | --- | --- |
| B1_Fields | Blue | Type 1 (blue) | Field | 
| G1_Forest | Green | Type 2 (cyan) | Forest
| R1_Dirt |Red | Type 3 (green) | Dirt/Roads

Secondary layers (`tx*_2.dds`)
| Code  | Color | UG mode color | Used for |
| --- | --- | --- | --- |
| B2_Water | Blue | Type 1 (Yellow) | Water
| G2_LightForest | Green | Type 2 (Red) | Light forest
| R2_Pavement | Red | Type 3 (Pink) | Pavement

Procedure:

- Add minimap or hemimap (plan) as layers. These will be used as guide to paint the detail layers.
- Create a new layer, fill with red and create a new "all hidden" layer mask: Layer > New layer mask > All hidden
- Select the layer mask and paint the areas.
- Repeat with green and blue colors.
- Clean the layers: colors can't intersect. Remove the intersection areas selecting a layer mask > left click > Copy area to selection. Then, left click another layer mask, "Intersect layer with selection". Finally, fill the selection with black.
- Repeat with secondary layers. 



FH2 discord > Mapping https://discord.com/channels/341977339623636993/898303257313697812/1190945346935865455