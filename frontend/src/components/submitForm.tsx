import { useState } from "react"

function queryData() {
    const [distance, setDistance] = useState()
    const [items, setItems] = useState()
    const [value, setValue] = useState()

    const handleClick = () => {
        setItems(items)
        setDistance(distance)
        setValue(value)
    }
    return (
        <div>
            <label>
                Item amount:
                <input type="text" name="items"/>
            </label>
            <input type="submit" value="Submit"/>
            <label>
                Distance:
                <input type="text" name="delivery_distance"/>
            </label>
            <input type="submit" value="Submit"/>
            <label>
                Cart value:
                <input type="text" name="cart_value"/>
            </label>
            <input type="submit" value="Submit"/>

            <button onClick={handleClick}>Calculate delivery price</button>
        </div>
    )
}

export default queryData