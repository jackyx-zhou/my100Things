import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import MyTable from "./MyTable";
import MyNavbar from "./MyNavbar"

const App = () => (
  <div>
    <MyNavbar />
    <div className="container">
      <DataProvider endpoint="api/clothes/"
                  render={data => <MyTable data={data} />} />
    </div>
  </div>
);
const wrapper = document.getElementById("root");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
