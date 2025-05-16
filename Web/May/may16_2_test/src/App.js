import logo from './logo.svg';
import './App.css';
import MyH1 from './myH1';
import MyH2 from './myP';
import MyTable from './myTable';
import Kekeke from './kekeke';

// Node.js서버에 업로드 되어서 실행
// Node.js가 기본적으로 포트번호를 3000쓰니까
// 포트번호 수정 : package.json -> "start": "set PORT=9999 && react-scripts start", set PORT=9999 && 이부분 추가하면됨 start에
// OOP를 구사함으로써 얻는 이득 : 소스 재사용
//    이름/나이 속성있고, 짖기/정보출력 기능있는 개를 여럿만들기 편하지

function App() {
  return (
    <>
      <MyH1></MyH1>
      <MyH1></MyH1>
      <MyH2></MyH2>
      <MyH2></MyH2>
      <MyTable></MyTable>
      <Kekeke></Kekeke>
    </>
  );
}

export default App;