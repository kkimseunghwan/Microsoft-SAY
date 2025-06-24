import React, { useState } from "react";
import Axios from "axios";
import { Link, Outlet } from "react-router-dom";
import "./siteLayout.css";

// redux (state 상태 관리해주는 애)

const SiteLayout = () => {
  return (
    <>
      <table className="site-table">
        <tr>
          <td>
            <h2>SiteLayout</h2>
          </td>
        </tr>
        <tr>
          <td>
            <Link to="/">홈</Link> &nbsp;&nbsp;
            <Link to="/gallery.go">갤러리</Link> &nbsp;&nbsp;
            <Link to="/notice.go">공지사항</Link>
          </td>
        </tr>
        <tr>
          <td>
            <Outlet />
          </td>
        </tr>
      </table>
    </>
  );
};

export default SiteLayout;
