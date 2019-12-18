def content(test_details,status,total_pass_asserts,total_pass_verify,total_fail_asserts,total_fail_verify):
    c='''
    <!--Dashboard-->
    <div id="dashboard" class="wrapper">
			<div class="container-fluid">
				<section  class="pading">
                    <div class="row mt-3">
						<div class="col-sm-12 col-lg-8">
							<div class="chart p-2 p-md-4 ">
								<span class="badge badge-secondary" data-toggle="tooltip pointer" data-placement="right" title="Execution timeline of each sample_test">Timeline</span>
								<br/>
								<br/>
								<p class="text-center pb-4 "><b>'''+test_details["duration"]+'''(H:MM:SS)</b> Overall Duration, <b>'''+str(status[4])+'''</b> total sample_test(s)</p>
								<canvas id="timelinechart" width="550" height="156" ></canvas>
							</div>
                        </div>
                        <div class="col-sm-12 col-lg-4">
                            <div class="chart p-2 p-md-4">
								<span class="badge badge-secondary"  data-toggle="tooltip pointer" data-placement="right" title="Test execution status breakdown">Status</span>
								<!--<br/>
								<br/>-->
								<p class="text-center pb-0 pb-md-1 pb-sm-1 pb-lg-1 "> <b>'''+str(status[0])+'''</b> sample_test(s) passed, <b>'''+str(status[1])+'''</b> failed, <b>'''+str(status[2])+'''</b> skipped, <b>'''+str(status[3])+'''</b> broken</p>   
                                <div style="position: relative">
									<p class="font-weight-bold" style="color:#28a745; position:absolute; top: 92px; left: 100px; font-size: 50px;" >'''+str(status[5])+'''%</p>
									<canvas id="statuschart" height="187" ></canvas>
								</div>
							</div>
                        </div>
                    </div>
				</section>
				<section  class="pading">
                    <div class="row mt-3">
						<div class="col-sm-12 col-lg-4">
							<div class="chart p-2 p-md-4 ">
								<span class="badge badge-secondary"  data-toggle="tooltip pointer" data-placement="right" title="Test execution status breakdown on Priority of sample_test cases">Priority</span>
								<br/>
								<br/>
                                <p class="text-center  pb-0 pb-md-2 pb-sm-2 pb-lg-4 "> <b>'''+str(status[4])+'''</b> total sample_test(s)</p>
                                <canvas id="prioritychart" height="187" ></canvas>
							</div>
                        </div>
                        <div class="col-sm-12 col-lg-4">
                            <div class="chart p-2 p-md-4">
								<span class="badge badge-secondary" data-toggle="tooltip pointer" data-placement="right" title="Assertion status breakdown on Severity of assertion steps">Assertion</span>
								<br/>
								<br/>
								<p class="text-center pb-0 pb-md-2 pb-sm-2 pb-lg-4 "> <b>'''+str(total_pass_asserts)+'''</b> assertion(s) passed, <b>'''+str(total_fail_asserts)+'''</b> assertion(s) failed</p>   
                                <canvas id="assertionchart" height="187" ></canvas>
                            </div>
                        </div>
						<div class="col-sm-12 col-lg-4">
                            <div class="chart p-2 p-md-4">
								<span class="badge badge-secondary" data-toggle="tooltip pointer" data-placement="right" title="Verification status breakdown on Severity of verification steps">Verifications</span>
								<br/>
								<br/>
								<p class="text-center pb-0 pb-md-2 pb-sm-2 pb-lg-4 "> <b>'''+str(total_pass_verify)+'''</b> verification(s) passed, <b>'''+str(total_fail_verify)+'''</b> verification(s) failed</p>   
                                <canvas id="verificationchart" height="187" ></canvas>
                            </div>
                        </div>
                    </div>
				</section>
				<!-- CARD -->
				<section  class="pading">
					<div class="row mt-1">
					<!--Details-->
						<div class="col-md-12 col-lg-6">
							<div class="row mt-3 ">
								<div class="col-md-3 col-lg-12 ">
									<div class="box-table">
										<table class="table table_ text-uppercase">
											<tbody>
												<tr>
													<td>Test Name</td>
													<td>'''+test_details["test_execution_name"]+'''</td>
												</tr>
												<tr>
													<td>Application Name</td>
													<td>'''+test_details["application_name"]+'''</td>
												</tr>
												<tr>
													<td>Owner</td>
													<td>'''+test_details["owner"]+'''</td>
												</tr>
												<tr>
													<td>Environment</td>
													<td>'''+test_details["environment"]+'''</td>
												</tr>
												<tr>
													<td>Browser</td>
													<td>'''+test_details["browser_name"]+''' '''+test_details["browser_version"]+'''</td>
												</tr>
												<tr>
													<td>OS</td>
													<td>'''+test_details["os"]+''' '''+test_details["os_version"]+'''</td>
												</tr>
											</tbody>
										</table>
									</div>
								</div>
							</div>
						</div>
						<div class="col-md-12 col-lg-6">
							<div class="row mt-3">
								<div class="col-md-3 col-lg-6">
									<div class="box">
										<div class="row">
											<div class=" col-6 col-lg-6">
												<h6 class="text-center" style="  background-color: #F1646C;">Test</h6>
											</div>
											<div class=" text-right col-6 col-lg-6">
												<span class="icon-flask pr-3"></span>
											</div>
											<p class="pl-3">'''+str(status[4])+'''</p>
										</div>
									</div>
								</div>
								<div class="col-md-3 col-lg-6">
									<div class="box">
										<div class="row">
											<div class="col-md-6 col-6">
												<h6 class="text-center"  style="  background-color: #1ECAB8;">Duration</h6>
											</div>
											<div class="col-md-6 col-6 text-right">
												<span class="icon-stopwatch"></span>
											</div>
											<p class="pl-3">'''+test_details["duration"]+'''(H:MM:SS)</p>
										</div>
									</div>
								</div>
							</div>
							<div class="row mt-3">
								<div class="col-md-3 col-lg-6">
									<div class="box">
										<div class="row">
											<div class="col-md-6 col-6">
												<h6 class="text-center"  style="  background-color: #4AC7EC;">Start</h6>
											</div>
											<div class="col-md-6 col-6 text-right">
												<span class="icon-clock"></span>
											</div>
											<p class="pl-3">'''+test_details["start_time"]+'''</p>
										</div>
									</div>
								</div>
								<div class="col-md-3 col-lg-6">
									<div class="box">
										<div class="row">
											<div class="col-md-6 col-6">
												<h6 class="text-center"  style="  background-color: #F3C74D;">End</h6>
											</div>
											<div class="col-md-6 col-6 text-right">
												<span class="icon-alarm-clock"></span>
											</div>
											<p class="pl-3">'''+test_details["end_time"]+'''</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</section>
				<br/>
				<br/>
			</div>
		</div>
    '''
    return c