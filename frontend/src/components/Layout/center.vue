<style>
</style>
<template>
  <div id="centre">
    <el-row>
      <stockprice></stockprice>
    </el-row>
  </div>
</template>

<script>
import stockprice from '../MainPage/StockPrice'
export default{
    name: 'centre',
    components:{
      stockprice
    }

}
</script>
