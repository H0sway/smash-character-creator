// Import dependencies
import React from 'react';

// Functional component that will track each individual move.
const AddMove = (props) => {
  return (
    <div className="Add-Move">
      <label>Attack Name:</label>
      <input
        type="text"
        name={props.attackName}
        value={props.attackValue}
        onChange={props.handleChange}
        required
      />

      <br />

      <label>Description</label>
      <textarea
        name={props.descriptionName}
        value={props.descriptionValue}
        onChange={props.handleChange}
        required
      />

      <br />

      <label>Add an image!</label>
      <input
        type="file"
        accept="image/*"
        name={props.moveImage}
        value={props.imageValue}
        onChange={props.handleChange}
        required
      />
    </div>
  )
}

export default AddMove;
