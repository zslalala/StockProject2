<style scoped>
  .el-aside{
    display: flex;
    justify-content: center;
    align-items: center;
  }

  section{
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding:10px;
  }

  .logo{
    height:auto;
  }

  .headerLogo,.logo{
    cursor: pointer;
  }
</style>

<template>
  <el-container>
    <el-aside width="auto" class="header-logo tap" >
      <h2>测试系统</h2>
    </el-aside>
    <el-aside width="auto" class="header-logo tap" >
      <el-avatar icon="el-icon-user-solid" class="headerLogo"></el-avatar>
    </el-aside>
  </el-container>
</template>

<script>
export default {
  data(){
    return {
      activeIndex:'1'
    };
  },
  methods:{
    handleSelect(key,keyPath){
      console.log(key,keyPath)
    }
  }
}
</script>












