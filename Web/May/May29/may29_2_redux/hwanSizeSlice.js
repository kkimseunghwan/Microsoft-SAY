// state : 상태
// reducer : 상태+액션 입력받아서 새로운 상태를 리턴하는 함수

// slice

// rxslice
import React, { PureComponent } from "react";
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  fontSize: 30,
};

const HwanSizeSlice = createSlice({
  name: "kss",
  initialState,
  reducers: {
    bigger: (curState) => {
      curState.fontSize += 10;
    },
    smaller: (curState) => {
      curState.fontSize -= 10;
    },
  },
});

export const {} = HwanSizeSlice.actions;
