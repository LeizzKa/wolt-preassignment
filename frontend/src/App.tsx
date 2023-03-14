import { useState, useEffect } from "react";
import DateTimePicker from "react-datetime-picker";
import axios from "axios";
import Header from "./components/topBar";
import "./App.css";

interface Props {
  items: number;
  distance: number;
  value: number;
  fees: number;
}

function App(props: Props) {
  const [fees, setFees] = useState();
  const [distance, setDistance] = useState();
  const [value, setValue] = useState();
  const [items, setItems] = useState();
  const [time, onChange] = useState(new Date());

  const handleDistanceChange = (event) => {
    setDistance(event.currentTarget.value);
  };
  const handleItemsChange = (event) => {
    setItems(event.currentTarget.value);
  };
  const handleValueChange = (event) => {
    setValue(event.currentTarget.value);
  };

  const fetch = async () => {
    const response = await axios.get(`${targetURL}`);
    setFees(response.data.total_fees);
  };

  let targetURL =
    "http://localhost:5000/item_amount=" +
    items +
    "&delivery_distance=" +
    distance +
    "&cart_value=" +
    value;

  return (
    <div className="App">
      <Header />
      <div className="Cart">
        <label>
          Cart value:
          <input
            id="cart_input"
            type="text"
            name="cart_value"
            value={value || ""}
            onChange={handleValueChange}
          />
        </label>
      </div>
      <div className="Distance">
        <label>
          Distance:
          <input
            id="distance_input"
            type="text"
            name="delivery_distance"
            value={distance || ""}
            onChange={handleDistanceChange}
          />
        </label>
      </div>
      <div className="Items">
        <label>
          Item amount:
          <input
            type="text"
            name="item_amount"
            value={items || ""}
            onChange={handleItemsChange}
          />
        </label>
      </div>
      <div className="Date">
        <DateTimePicker
          onChange={onChange}
          value={time}
          format="y-MM-dd h:mm:ss"
        />
      </div>
      <div className="submit-button">
        <button
          id="submit"
          onClick={(e) => {
            handleValueChange;
            handleDistanceChange;
            handleItemsChange;
            fetch();
          }}
        >
          Calculate delivery price
        </button>
      </div>
      <div className="delivery">
        <p>Delivery price: </p>
        <p>{(Math.round(fees) / 100).toFixed(2) || null}</p>
      </div>
    </div>
  );
}

export default App;
