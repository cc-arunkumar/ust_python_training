export default function Hello({ colorname }){
    return(
        <div className={`card ${colorname}`}>
        <h3 className="font">Hello Browser!</h3>
        <p className="font">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat, voluptatum.</p>
        </div>
    )
}