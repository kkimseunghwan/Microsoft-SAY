import logo from "./logo.svg";
import "./App.css";
import HwanEchoClient from "./socket/hwanEchoClient";
import HwanEchoClient2 from "./socket/hwanEchoClient2";
import HwanDrawClient from "./socket/hwanDrawClient";
function App() {
  return (
    <>
      {/* <HwanEchoClient /> */}
      {/* <HwanEchoClient2 /> */}
      <HwanDrawClient />
    </>
  );
}

export default App;

// 배포
// 그 프로젝트로 가서 cmd 창 열고
// yarn build
// 그러면 그 프로젝트 폴더 안에 build 폴더가 생기고 그 안에 파일들이 생김
// 그러면 그 파일들을 그대로 복사해서 배포하면 됨
