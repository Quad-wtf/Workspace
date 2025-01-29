import "./userInfo.css";

const UserInfo = () => {
   return (
      <div className="userInfo">
         <div className="user">
            <img src="./avatar.png" draggable="false"/>
            <h2>Quad</h2>
         </div>
         <div className="icons">
            <img src="./more.png" draggable="false"/>
            <img src="./video.png" draggable="false"/>
            <img src="./edit.png" draggable="false"/>
         </div>
      </div>
   )
}

export default UserInfo