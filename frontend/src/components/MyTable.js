import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import Table from "react-bootstrap/Table"

const headingStyles = {
  textTransform: "capitalize"
}

const MyTable = ({ data }) =>
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <h2 className="subtitle">
        Showing <strong>{data.length} items</strong>
      </h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            {Object.entries(data[0]).map(el => <th key={key(el)} style={headingStyles}>{el[0]}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map(el => (
            <tr key={el.id}>
              {Object.entries(el).map(el => <td key={key(el)}>{el[1].toString()}</td>)
              }
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
MyTable.propTypes = {
  data: PropTypes.array.isRequired
};
export default MyTable;
