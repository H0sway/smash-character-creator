// Import dependencies
import React from 'react';

// Functional component, will track all the changes for the data that will be sent to the Character api route.
const AddCharacter = (props) => {
  return (
    <div className="Add-Character">
      <label>Character Name:</label>
      <input
        type="text"
        name="name"
        value={props.nameValue}
        onChange={props.handleChange}
        required
      />

      <br />

      <label>Character Series:</label>
      <input
        type="text"
        name="series"
        value={props.seriesValue}
        onChange={props.handleChange}
        required
      />

      <br />

      <label>Description:</label>
      <textarea
        name="description"
        value={props.descriptionValue}
        onChange={props.handleChange}
        required
      />

      <br />

      <label>Add an image!</label>
      <input
        type="file"
        accept="image/*"
        name="image"
        value={props.characterImage}
        onChange={props.handleChange}
        required
      />
    </div>
  )
}

export default AddCharacter;
